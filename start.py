#!/usr/bin/python3

from flask import Flask, redirect, url_for, request, render_template
import json
import numpy as np

app = Flask(__name__)

@app.route('/')

def home():
  return render_template("base.html")

@app.route("/total",methods=["POST", "GET"])
def sumlist():
    a=list(range(10000001))
    b=sum(a)
    c={"total":b}
    f=json.dumps(c)
    return render_template('response.html',msg=f,request="Get total of a given list")
    
@app.route("/total_order",methods=["POST", "GET"])
def  total_order():
    # as an illustration, the customer orders is set as a list of random
    # number, in real application, this data can come from  a database
    # here we use numpy operation to speed up calculation
    mu,sigma=100,20
    order=np.random.normal(mu,sigma,10000001)
    # order cannot be negative
    order[order<0]=0
    total=np.sum(order)
    total=int(total)
    c={"total customer order":total}
    f=json.dumps(c)
    return render_template('response.html',msg=f,request="Total customer order")

@app.route("/average_order",methods=["POST", "GET"])
def  average_order():
    # get the average customer order, in real application, this data can come from a database
    # or some kind of statistics calculations
    # for very large list, it is expected that the average will be mu: this is just an illustration
    mu,sigma=100,20
    order=np.random.normal(mu,sigma,10000001)
    # order cannot be negative
    order[order<0]=0
    total=np.sum(order)
    average=total/10000001.0
    average=round(average,2)
    c={"average customer order":average}
    f=json.dumps(c)
    return render_template('response.html',msg=f,request="Average customer order")

@app.route("/max_order",methods=["POST", "GET"])
def  max_order():
   # get the maximum customer orders
   mu,sigma=100,20
   order=np.random.normal(mu,sigma,10000001)
   # order cannot be negative
   order[order<0]=0
   vmax=np.max(order)
   vmax=round(vmax,2)
   c={"maximum customer order":vmax}
   f=json.dumps(c)
   return render_template('response.html',msg=f,request="Maximum customer order")
   
@app.route("/top10_order",methods=["POST", "GET"])
def  top10_order():
     #  get a list of top 10 customer orders
     mu,sigma=100,20
     order=np.random.normal(mu,sigma,10000001)
     order[order<0]=0
     order=np.sort(order,kind="mergesort")
     sublist=order[9999991:10000001]
     sublist=np.flipud(sublist)
     d=[round(v,2) for v in sublist]
     b={"top 10 order":d}
     f=str(b)
     return render_template('response.html',msg=f,request="List of top 10 orders")

@app.route("/top10_customer",methods=["POST", "GET"])
def  top10_customer():
     #  get a list of 10 customer id with top orders
     mu,sigma=100,20
     order=np.random.normal(mu,sigma,10000001)
     order[order<0]=0
     order=np.argsort(order,kind="mergesort")
     sublist=order[9999991:10000001]
     d=np.flipud(sublist)
     b={"top 10 customer id":d}
     f=str(b)
     return render_template('response.html',msg=f,request="List of 10 customer index with top orders")



@app.route("/higher_order",methods=["POST", "GET"])
def  higher_order():
     #  get number of customers with order >= some value
     value=190
     if (request.method=="POST"):
        result=request.form
        value=float(result["value"])
     mu,sigma=100,20
     order=np.random.normal(mu,sigma,10000001)
     order[order<0]=0
     order=np.sort(order,kind="mergesort")
     vmax=order[10000000]
     vmin=order[0]
     nn=0
     if (value<=vmin) :
         nn=10000001
     elif (value>vmax)  :
         nn=0
     else:
        it=np.argmax(order>=value)
        nn=10000001-it
     b={"number of higher order":nn}
     f=str(b)
     req="number of customers with order>="+str(value)
     return render_template('response.html',msg=f,request=req)


if __name__ == "__main__":
  app.run(debug=False)
    
