# python-tokenizer
### Build and run docker container with Flask RESTful API for interacting with NLP-IE tokenizer service

Clone repo `git clone https://github.com/nlpie/python-tokenizer`

Chande directory `cd python-tokenizer`

Build image `docker build --tag=python-tokenizer .` 
  
Run container and publish port 5000, allowing code changes to app.py to restart flask with the new changes
`docker run -it --publish=5000:5000 --env="MODE=dev" --volume=$PWD:/app:ro python-tokenizer`
  
API should be accessible on port 5000   
  `curl -XPOST -i localhost:5000/analyze`
  
  `curl -XPOST -i localhost:5000/process/{event_id}/{document_id}`
