import RPi.GPIO as GPIO
import time
import sys

LED_GREEN=17
LED_RED=18

def init_gpio():
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(LED_GREEN,GPIO.OUT)
   GPIO.setup(LED_RED,GPIO.OUT)
   GPIO.output(LED_GREEN,GPIO.LOW)
   GPIO.output(LED_RED,GPIO.LOW)

def led_feedback(is_correct):
   if is_correct:
      GPIO.output(LED_GREEN,GPIO.HIGH)
      time.sleep(1)
      GPIO.output(LED_GREEN,GPIO.LOW)
   else:
      GPIO.output(LED_RED,GPIO.HIGH)
      time.sleep(1)
      GPIO.output(LED_RED,GPIO.LOW)

def quiz():
  print("Welcome to the python Quiz!")
  print("Answer the follow question:")

questions=["1.Which of the following is NOT a python data type?:a.int b.float c.rational d.string e.bool",
           "2.which of the following is NOT a built-in operation in python?:a.+ b.% c.abs() d.sqrt()",
           "3.In a mixed-type eapession involing ints and floats,python will convert:a.floats to ints b.ints to strings c.floats and ints to strings d.ints to floats",
           "4.The best structure for implementing a muiti-way decision in Python is:a.if b.if-else c.if-elif-else d.try",
           "5.What statement can be executed in the body of a loop to cause it to terminate? a.if b.exit c.continue d.break"
          ]
answers=["c",
         "d",
         "d",
         "c",
         "d"
        ]
score=0

init_gpio()

quiz()

for i in range(len(questions)):
      user_answer=input(questions[i]).strip().lower()
      if user_answer==answers[i]:
          print("Correct!")
          score+=1
          led_feedback(is_correct=True)
      else:
          print("Incorrect!")
          led_feedback(is_correct=False)

print("\nQuiz completed!")
print(f"You got {score}/{len(questions)} question correct.")

