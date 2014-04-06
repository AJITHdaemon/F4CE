from kivy.app import App
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.label import Label 
from kivy.uix.button import Button 
from kivy.uix.spinner import Spinner
from kivy.uix.slider import Slider 
from kivy.uix.image import Image
from kivy.uix.bubble import Bubble

class MyApp(App):
  def build(self):
  	f=FloatLayout(size=(780,1280))
  	b=Button(text="",
  		opacity=0.5,
  		background_color=(0.5,1,0,1),
  		color=(1,1,1,1),
  		font_size='30sp',
  		size_hint=(.09 , .1),
  		pos_hint={'x':.02,'y':.15},
		border='5sp')
  	c=Button(text="",
  		opacity=0.5,
  		background_color=(0.5,1,0,1),
  		color=(1,1,1,1),
  		font_size='30sp',
  		size_hint=(.09 , .1),
  		pos_hint={'x':.2,'y':.15},
		border='5sp')
  	d=Button(text="",
  		opacity=0.5,
  		font_size='30sp',
  		background_color=(1,1,0,1),
  		color=(1,1,1,1),
  		size_hint=(.09 , .1),
  		pos_hint={'x':.11,'y':.25},
		border='5sp')
  	e=Button(text="",
  		opacity=0.5,
  		font_size='30sp',
  		background_color=(1,1,0,1),
  		color=(1,1,1,1),
  		size_hint=(.09 , .1),
  		pos_hint={'x':.11,'y':.05},
		border='5sp')
    	g=Button(text="",
      		opacity=0.3,
      		background_color=(0.5,1,0,1),
      		color=(1,1,1,1),
      		font_size='30sp',
     		size_hint=(.09 , .1),
      		pos_hint={'x':.91,'y':.15},
		border='5sp')
    	h=Button(text="",
      		opacity=0.3,
      		background_color=(0.5,1,0,1),
      		color=(1,1,1,1),
      		font_size='30sp',
      		size_hint=(.09 , .1),
      		pos_hint={'x':.73,'y':.15},
		border='5sp')
    	i=Button(text="",
      		opacity=0.3,
      		font_size='30sp',
      		background_color=(1,1,0,1),
      		color=(1,1,1,1),
      		size_hint=(.09 , .1),
      		pos_hint={'x':.82,'y':.25},
		border='5sp')
    	j=Button(text="",
      		opacity=0.3,
      		font_size='30sp',
      		background_color=(1,1,0,1),
      		color=(1,1,1,1),
      		size_hint=(.09 , .1),
      		pos_hint={'x':.82,'y':.05},
		border='5sp')
	im1=Image(source='left.png',
		size_hint=(.09,.1),
		pos_hint={'x':.02,'y':.15})
	im2=Image(source='right.png',
		size_hint=(.09,.1),
		pos_hint={'x':.2,'y':.15})
	im3=Image(source='up.png',
		size_hint=(.09,.1),
		pos_hint={'x':.11,'y':.25})
	im4=Image(source='down.png',
		size_hint=(.09,.1),
		pos_hint={'x':.11,'y':.05})
	im5=Image(source='o.png',
		size_hint=(.09,.1),
      		pos_hint={'x':.91,'y':.15})
	im6=Image(source='x.png',
		size_hint=(.09,.1),
		pos_hint={'x':.73,'y':.15})
	im7=Image(source='x.png',
		size_hint=(.09,.1),
		pos_hint={'x':.82,'y':.25})
	im8=Image(source='o.png',
		size_hint=(.09,.1),
		pos_hint={'x':.82,'y':.05})
	im9=Image(source='p.png',
		size_hint=(.07,.08),
		pos_hint={'x':.45,'y':.05})
		
	
	f.add_widget(im1)
	f.add_widget(im2)
	f.add_widget(im3)
	f.add_widget(im4)
	f.add_widget(im5)
	f.add_widget(im6)
	f.add_widget(im7)
	f.add_widget(im8)
  	f.add_widget(b)
  	f.add_widget(c)
  	f.add_widget(d)
  	f.add_widget(e)
    	f.add_widget(g)
    	f.add_widget(h)
    	f.add_widget(i)
    	f.add_widget(j)
  	
    

  	return f

if __name__ == '__main__':
	MyApp().run()
