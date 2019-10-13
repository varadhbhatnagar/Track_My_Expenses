import cloudmersive_ocr_api_client
from cloudmersive_ocr_api_client.rest import ApiException

api_instance = cloudmersive_ocr_api_client.ImageOcrApi()
image_files = ['Bill Samples/1.jpeg','Bill Samples/2.png','Bill Samples/3.png','Bill Samples/4.jpg'] # file | Image file to perform OCR on.  Common file formats such as PNG, JPEG are supported.
api_instance.api_client.configuration.api_key = {}
api_instance.api_client.configuration.api_key['Apikey'] = '3322d54e-4159-4707-b664-234dcda15445'

for image in image_files:
    try:
        # Converts an uploaded image in common formats such as JPEG, PNG into text via Optical Character Recognition.
        api_response = api_instance.image_ocr_photo_recognize_receipt(image, recognition_mode='Advanced', preprocessing='Advanced')
        print(api_response)
    except ApiException as e:
        print("Exception when calling ImageOcrApi->image_ocr_post: %s\n" % e)