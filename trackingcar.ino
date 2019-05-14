int trig = 8; // 出力ピン
int echo = 9; // 入力ピン

void setup() {

//setup of ultrasonic mosule
Serial.begin(9600);
pinMode(13,OUTPUT);
pinMode(trig,OUTPUT);
pinMode(echo,INPUT);

  
}

// d means distance from hand to car
float d; 


//danger means close distance
float danger1 = 0;
float danger2 = 5.0;
float danger3 = 10.0;
float danger4 = 15.0;

// c means counter of [for loop]
byte c;





void loop() {
  
// 超音波の出力を初期化
digitalWrite(trig,LOW);
delayMicroseconds(1);

// 超音波を出力
digitalWrite(trig,HIGH);
delayMicroseconds(11);

// 超音波を出力終了
digitalWrite(trig,LOW);

// 出力した超音波が返って来る時間を計測し入力
int t = pulseIn(echo,HIGH);

// 計測した時間と音速から対象までの距離を計算
d = t*0.017;

//実際の数値をシリアルモニタで確認(単位はcm)
Serial.print(d);
Serial.println(" cm");


//モーターの出力が調整できなさそうなので、モーター起動頻度で平均速度をコントロールする
//各場合におけるモーターが動く時間(と止まっている時間の合計)は同じであることが望ましい
if(d >= danger4)
{
  // go 
  
  analogWrite(13,128);
  delay(600);
}

else if(d >= danger3 && d <= danger4)
{
  //slow down
  //example for half speed

  for(c = 0;c <= 3;c++)
  {
   analogWrite(13,128);
   delayMicroseconds(100);
   analogWrite(13,0);
   delayMicroseconds(100);
  }  
}
else if(d >= danger2 && d <= danger3)
{
  //super slow down
  
  for(c = 0;c <= 3;c++)
  {
    analogWrite(13,128);
    delayMicroseconds(150);
    analogWrite(13,0);
    delayMicroseconds(50);
  }    
}

else if(d >= danger1 && d <= danger2)
{
  //stop
  
    analogWrite(13,0);
    delayMicroseconds(600);
}


}
