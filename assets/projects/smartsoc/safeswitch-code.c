#include <LiquidCrystal_I2C.h>
#include <BluetoothSerial.h>

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

BluetoothSerial SerialBT;


byte Introbullet[8] = {
  
 0b11000,
 0b11100,
 0b11110,
 0b11111,
 0b11111,
 0b11110,
 0b11100,
 0b11000  
  
  };
  

const int up = 34,enter=32,left=36,right=39,down=35,back=33, buzzer = 26, relay = 18;
byte hr=0,mins=0,sec=0;
byte crs = 0;
byte crsPos = 0;
String t = String(hr)+":"+String(mins)+":"+String(sec);
boolean once2 = false;
long dcdCT = 0;
byte page = 0;
boolean gst = false,once1 = false, Pause = false, alert = false;
long startTime = 0, timeSpent = 0, duration = 0;
String rTime = "";

byte alertD = 0; 


LiquidCrystal_I2C lcd(0x27,16,2);



void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
    lcd.init();
  lcd.backlight();
  pinMode (buzzer,OUTPUT);
  pinMode(relay,OUTPUT);
  pinMode(up,INPUT);
  pinMode(down,INPUT);
  pinMode(right,INPUT);
  pinMode(left,INPUT);
  pinMode(enter,INPUT);
  pinMode(back,INPUT);
  digitalWrite(buzzer,HIGH);
  delay(500);
  digitalWrite(buzzer,LOW);
  Mprint("SmartSoc",3,0);
  SerialBT.begin("SmartSoc");
  lcd.createChar(0,Introbullet);


}

void loop() {
  // put your main code here, to run repeatedly:

  bluetoothFunc();

   if (page == 0) select1();
   else if (page == 1) setTime();
   else if (page == 2) countDown();
   else if (page == 3) PauseFunc();
   else if (page == 4) routine();

   if (alert && alertD <= 10){

          digitalWrite (buzzer,HIGH);
          delay(1000);
          digitalWrite (buzzer,LOW);
          alertD++;
      
    }

   if (alertD >= 10){
    alert = false;
    alertD = 0;
    }
  
}

byte br = 0;
void select1(){
  lcd.noBlink();
  control2();
  lcd.setCursor(0,br);
  lcd.write(0);
  Mprint("Timer",1,0);
  Mprint("Routine",1,1);
  
  
  }

 void control2(){
  lcd.clear();
  if(digitalRead(down) == LOW){
    delay(65);

    br = 1;
    }

    if(digitalRead(up) == LOW){
    delay(65);

    br = 0;
    }

     if(digitalRead(enter) == LOW && br == 0){
    delay(65);
    page = 1;
    
    }

    else if(digitalRead(enter) == LOW && br == 1){
    delay(65);
    page = 4;
    
    }
  
  }

  bool wordPr(String w, String t){
    t.toLowerCase();
    if (t.indexOf(w) >= 0) return true;
    else return false;
       
    }

void bluetoothFunc(){
  
  if (SerialBT.available()) {
    String cmd = SerialBT.readString();
    
    if (cmd.equals("a") || (wordPr(" on ",cmd) && (wordPr("switch",cmd) || wordPr("turn",cmd) || wordPr("put",cmd)))) {
      digitalWrite(relay, HIGH); // Turn on the relay
      Serial.println("Relay ON");
    } else if (cmd.equals("b") || (wordPr(" off ",cmd) && (wordPr("switch",cmd) || wordPr("turn",cmd) || wordPr("put",cmd)))) {
      digitalWrite(relay, LOW); // Turn off the relay
      Serial.println("Relay OFF");
    }
  }

  delay(20);
  
  }

void routine(){
  Mprint("Set Routine",0,1);

  if (digitalRead(back) == LOW){
            delay(65);
            page = 0;
        
        }
  
  }

void countDown(){

  if (!gst){
    
      startTime = millis();
      gst = true;
    }

    timeSpent = millis() - startTime;
    digitalWrite(relay,HIGH);
   if (timeSpent >= duration){

        gst = false;
        Pause = false;
        alert = true;
        once1 = false;
        hr = 0; mins = 0; sec = 0;
        t = String(hr)+":"+String(mins)+":"+String(sec);
       timeSpent = 0;
       duration = 0;
        lcd.clear();
        page = 1;
       
     digitalWrite(relay,LOW);
 
    }
   


      if(digitalRead(back) == LOW) {
        delay(200);
        Serial.println("back");
        alert = false;
        gst = false;
        Pause = false;
        once1 = false;
        alertD = 0;
        hr = 0; mins = 0; sec = 0;
        t = String(hr)+":"+String(mins)+":"+String(sec);
        timeSpent = 0;
       duration = 0;
       lcd.clear();
        page = 1; 
        digitalWrite(relay, LOW);      
        
        } 


     else if(digitalRead(enter) == LOW) {
      delay(300);
        Serial.println("enter");

            Pause = true;

            if (Pause){

              duration = duration - timeSpent;

              once1 = true;
              gst = false;
              page = 3;

              lcd.clear();
              
              }
        
        
        } 
        
    


      if (!once2){

        dcdCT = millis();

        once2 = true;
        
        }
        


    rTime = S_HMS(duration - timeSpent);
     
     if ((millis() -dcdCT) >= 1000) {
      lcd.clear();
      Mprint("Time left:",3,0);
      Mprint(rTime,4,1);

      once2 = false;

     }
  
  
  
  }


void PauseFunc(){

  lcd.clear();
  Mprint("PAUSED",3,0);
  Mprint(S_HMS(duration),4,1);

  
    
    
    if(digitalRead(enter) == LOW && page == 3) {
      
      delay(300);

          Serial.println("enter");

              Pause = false;
              lcd.clear();
              page = 2;
          
        }
    
  

  
  }





void setTime(){

    control();
    Mprint("Set time",3,0);
    Mprint(t,4,1);
    
    if (crs == 0) Mcrs(3,t);
    else if (crs == 1) Mcrs(2,t);
    else Mcrs(1,t);

       
    delay(100);
  }

void Mcrs(byte p, String s){

      if (p == 1){      
        lcd.blink();
      lcd.setCursor(4,1);
        }
     else if (p == 2){
        int a =s.indexOf(':');
       lcd.blink();
      lcd.setCursor(4+a+1,1);
      }

     else{
      int a =s.lastIndexOf(':');
       lcd.blink();
      lcd.setCursor(4+a+1,1);
      
      }
    }

void control(){


        lcd.clear();
      if (digitalRead(up) == LOW && hr < 30 && crs == 2){
        delay(65);
        Serial.println("Up"); 
        hr+=1;
        if (hr > 30) hr = 0;
        t = String(hr)+":"+String(mins)+":"+String(sec);
      }
    else if (digitalRead(up) == LOW && mins < 59 && crs == 1){
      delay(65);
      Serial.println("Up");
        mins +=1;
        if (mins > 59) mins = 0;
         t = String(hr)+":"+String(mins)+":"+String(sec);
      }
    else if (digitalRead(up) == LOW && sec < 59 && crs == 0){
      delay(65);
      Serial.println("Up");
        sec +=1;
        if (sec > 59) sec = 0;
        t = String(hr)+":"+String(mins)+":"+String(sec);
    }

    else if (digitalRead(down) == LOW && hr < 30 && crs == 2 && hr !=0){ 
        delay(65);
        Serial.println("down");
        hr-=1;
        if (hr < 0) hr = 29;
         t = String(hr)+":"+String(mins)+":"+String(sec);
      }
    else if (digitalRead(down) == LOW && mins < 59 && crs == 1 && mins != 0){
        delay(65);
                Serial.println("down");

        mins -=1;
        if (mins < 0) mins = 59;
         t = String(hr)+":"+String(mins)+":"+String(sec);
      }
    else if (digitalRead(down) == LOW && sec < 59 && crs == 0 && sec != 0){
        delay(65);
                Serial.println("down");

        sec -=1;
        if (sec < 0) sec = 59;
         t = String(hr)+":"+String(mins)+":"+String(sec);
      }

    else if (digitalRead(left) == LOW){
          delay(65);
                  Serial.println("left");

          crs +=1;
          if (crs > 2) crs = 0;
           t = String(hr)+":"+String(mins)+":"+String(sec);

      }  


     else if (digitalRead(right) == LOW){
          delay(65);
                  Serial.println("right");

          crs -=1;
          if (crs < 0) crs = 2;
           t = String(hr)+":"+String(mins)+":"+String(sec); 
      }

      else if (digitalRead(enter) == LOW && page == 1){
               delay(65);
                       Serial.println("enter");

              duration = HMS_S(hr,mins,sec)*1000;

              page = 2;
          
        }


       else if (digitalRead(enter) == LOW){
            delay(65);
                    Serial.println("enter");

            hr = 0; mins = 0; sec =0;
            t = String(hr)+":"+String(mins)+":"+String(sec);
            page = 1;
        
        }

        else if (digitalRead(back) == LOW){
            delay(70);
             alertD = 0;
            page = 0;
            
        }

  }

long HMS_S(byte hr,byte mins, byte sec){

   int Tsec = 0;

   Tsec += sec;
   Tsec += (mins*60);
   Tsec += (hr*3600);
  
    return Tsec;
  }


String S_HMS(long s){

      s /= 1000;

     int iHr = s/3600;

     s -= (iHr*3600);

     int iMin = s/60;

     s -= (iMin*60);

     return String(iHr)+":"+String(iMin)+":"+String(s);
  
  }


void Mprint(String tx, byte c,byte r){
      lcd.setCursor(c,r);
      lcd.print(tx);      
    }

   