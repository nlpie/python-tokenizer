#python

from flask import Flask, jsonify, abort, make_response, request
import requests
from nltk.tokenize import WhitespaceTokenizer, RegexpTokenizer, WordPunctTokenizer

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def analyze( text ):
    # tokenize
    spans = WordPunctTokenizer().span_tokenize(text)

    #create index, populate, and add to list
    indexList = []
    annotationIndex = {
        "@type": "annotationIndex", #edu.umn.nlpie.micronaut.core.model.processingartifact.AnnotationIndex
        "name": "tokens",
        "annotations": []
    }
    for span in spans:
        begin = span[0]
        end = span[1]
        token = text[ begin:end ]
        annotationIndex['annotations'].append( {
            '@type':'genericMap', #edu.umn.nlpie.micronaut.core.model.annotation.GenericMap
            'token':token,
            'begin':begin,
            'end':end
        } )
    indexList.append( annotationIndex )
    return indexList


@app.route( '/analyze', methods=['POST'] )
def analyze_endpoint():
    # validateOptions is n/a - no options passes - skipping implementation formal impl of noop for brevity of this example service
    # get text from posted json
    json = request.get_json()
    text = json["text"]
    print("tokenizing:",text)
    indexList = analyze( text )
    return jsonify( indexList[0] ), 200

@app.route( '/process/<event_id>/<document_id>', methods=['POST'] )
def process_endpoint( event_id,document_id ):
    # validateOptions is n/a - no options passes - skipping implementation formal impl of noop for brevity of this example service
    # get text from event processing service
    url = "http://host.docker.internal:8081/event/text/{}/{}".format(event_id,document_id)
    r = requests.get(url)
    text = r.text   #"The rain falls mainly on the plain, observed by a theologian"
    print("tokenizing",text)

    indexList = analyze( text )

    for index in indexList:
        # post index to event processing service
        url = "http://host.docker.internal:8081/event/index/{}/{}".format(event_id,document_id)
        r = requests.post( url, json=index )
        print ("POST RESPONSE", r.status_code)

    return ('', 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
