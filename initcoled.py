#!/usr/bin/python3
#coding:utf-8

import pickle
import psycopg2
from cassandra.cluster import Cluster
from kafka import KafkaProducer
from multiprocessing import Process

import conf as co



class initcoled:

    def __init__(self):
        pg = psycopg2.connect("host='{host}' dbname='{dbname}' user='{user}' password='{password}'".format(host=co.pg_host,dbname=co.pg_base,user=co.pg_user, password=co.pg_password))
        self.cur = pg.cursor()
        cluster = Cluster(co.ca_host,co.ca_port)
        self.session = cluster.connect()
        self.set_keyspace('pdrdata')
        self.producer = KafkaProducer(bootstrap_servers=co.ka_host)
        self.data = []


    def get_pgdata(self,table)
        self.cur.execute("SELECT id,face_descriptor FROM %s", [table,])
        self.data = self.cur.fetchall() 


    def writing_queue(self,queue):
        for row in data:
            self.producer.send(queue, pickle.dumps(pickle.dumps({'id':row[0],'discriptor':row[1]})))
        self.producer.flush()


def running(queue,table):
    i = initcoled(queue)
    i.get_pg_data(table)
    i.writing_queue(queue)





if __name__ == '__mail__':

    p1 = Process(target=running, args=('person','dim.person'))
    p1.start()
    p1.join()

    p2 = Process(target=running, args=('employee','dim.employee'))
    p2.start()
    p2.join()

