# python-tokenizer

### Build and run docker container with Flask RESTful API for interacting with example tokenizer service

Clone repo `git clone https://github.com/nlpie/python-tokenizer`

Change directory `cd python-tokenizer`

Build image `docker build --tag=python-tokenizer .` 
  
Run container and publish port 5000, allowing code changes to app.py to restart flask with the new changes
`docker run -it --publish=5000:5000 --env="MODE=dev" --volume=$PWD:/app:ro python-tokenizer`
  

### Invoking API interface enpoints

Generate an `AnnotationIndex` of tokens for some arbitrary POSTed text:

`curl -XPOST localhost:5000/analyze -H "Content-Type:application/json" -d '{"text":"Some text, here."}'`


Process text added to a `Document` associated with a previously registered `Event`. The `process` endpoint adds the generated `AnnotationIndex` to the referenced `Document` for later use:
  
`curl -XPOST localhost:5000/process/<event_id>/<document_id> -H "Content-Type:application/json" -d '{}'`

When invoking the `process` endpoint, the JSON document passed in is explicitly empty - no `PostBody` options attribute need be specified since the tokenizer's functionality is fixed and does not accept an options paramater.

### Example index created by the annotator
```javascript


{
   "tokens": {
      "@type": "annotationIndex",
      "name": "tokens",
      "annotations": [
         {
            "@type": "genericMap",
            "end": 8,
            "begin": 0,
            "token": "addendum"
         },
         {
            "@type": "genericMap",
            "end": 11,
            "begin": 9,
            "token": "to"
         },
         {
            "@type": "genericMap",
            "end": 15,
            "begin": 12,
            "token": "the"
         },
         {
            "@type": "genericMap",
            "end": 21,
            "begin": 16,
            "token": "above"
         },
         {
            "@type": "genericMap",
            "end": 26,
            "begin": 22,
            "token": "note"
         }
      ]
   }
}
```
