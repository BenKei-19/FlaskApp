# [PROJECT] Object Detection with YOLO + Flask + Railway

## [Server] To test the server, you can visit [this page] (https://flaskapp-production-4f78.up.railway.app/) 

## Introduction

I will deploy a normal model Yolov11, fine-tune with three classes that person, cat, car. Using flask and Railway to deploy online model. User can access to the page and upload an image, result will return an image with bounding box, class of this bounding box and confident.

## Datasets
[Coco Dataset 2017](https://cocodataset.org/#home)

## Notices
To run not local, i will use railway to deploy my model, simply HTML web for user can upload an image.
## Setting

* **First of all, i will try to deploy my model in local, i use Flask to do that by creating templates, it have index.html and writing app.py to get request**
* **Second, to deploy this model online, i will use railway.com to deploy this model. It require Dockerfile, requirements.txt**