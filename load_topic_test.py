#!/usr/bin/python3

import json
import pickle
import argparse

from kafka import KafkaProducer

import conf as co


def main():


    parser = argparse.ArgumentParser(prog='load_topic_test.py')
    parser.add_argument('topic', nargs=1, help='topic help')
    opt = parser.parse_args()
    topic = opt.topic[0]

    producer = KafkaProducer(bootstrap_servers=co.ka_host)
    


    with open('test_data.json') as f:
        n = 1
        for row in f.readlines():
            msg = {"id":n, "descriptor": json.loads(row)["face"]["descriptor"]}
            producer.send(topic, pickle.dumps(msg))
        
            n += 1

        producer.flush()
        
        
if __name__ == '__main__':
    main()
    
