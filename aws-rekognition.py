import boto3

# Let's use Amazon s3
s3 = boto3.resource('s3')

# Print out the bucket names
for bucket in s3.buckets.all():
	print(bucket.name)

data = open('test_img.jpg', 'rb')
s3.Bucket('aearanky-test-cli-s3').put_object(Key='test_img.jpg', Body=data)

# Upload and process the image and print the response
fileName='test_img.jpg'
bucket='aearanky-test-cli-s3'
    
client=boto3.client('rekognition')

response = client.detect_faces(Image={'S3Object':{'Bucket':bucket,'Name':fileName}})

print('Detected labels for ' + fileName)    
for label in response['FaceDetails']:
	print (str(label['BoundingBox']['Top']) + ' : ' + str(label['BoundingBox']['Left']))
