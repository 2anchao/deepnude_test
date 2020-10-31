# Deepnude_test.  
The source code is provide by deepnude official: https://github.com/stacklikemind/deepnude_official.  
Out of curiosity, I test this project in Mac env.

## Install env.  
python.       
opencv-python.   
torch(I use CPU).   
torchvision.    
numpy.   
wheel.   
six.  
...   
## Test Model.  
Link: https://pan.baidu.com/s/1GCLOVcvy55RulYcViRjGQQ  secret: 1wrw

## Result.  
The result show as follow, Left image is the origin photo, Right is the deepnude output result with added mosaic. 
<div align=left><img src="https://github.com/2anchao/deepnude_test/blob/main/img_show/show.jpeg" width="250" height="380"<div align=right><img src="https://github.com/2anchao/deepnude_test/blob/main/img_show/input1.jpg" width="250" height="380" /></div>. 

## Result Analysis. 
I test seris of photos, and conclusion as follow:   
(1) The train data is simple, maybe only have front side photo, so the other side photo can not get satisfied result.  
(2) If the backgroud of photo is too complex, result is also worse. 
(3) Deepnude has long way to go. 

## Attention.   
I just use the official code to test.    
I find the Dataloader build section will be seized up when run Main.py in my env, so I modified dataload method.    
This code only for technology share, anyone who what use in illegal way will be punished by law.     
Finally, thanks for Four big vegetables B provide test photos.     
