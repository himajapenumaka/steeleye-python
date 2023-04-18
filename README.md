# steeleye-python

There are three files in this repository, which are extractxml.py, xmltocsv.py and uploadtos3.py.
Among these, extractxml.py contains the code to downlaod the zip file from the given xml link and extract the xml file from this zip file.
The file xmltocsv.py contains the code to convert this XML file to CSV file (only specified elements/tags).
The file uploadtos3.py contains the code to upload the CSV file, obtained from the file xmltocsv.py, to S3 bucket.

Also, since the code involves external resources such as XML file and S3 bucket, I believe it's not ideal for unit testing. Unit tests should be isolated from external dependencies to ensure that the tests only verify the behavior of the code being tested and not the behavior of external services.
