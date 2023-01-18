from flask import Flask,jsonify,request
from pdf2docx import Converter
import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# import fileinput

app=Flask(__name__)

@app.route('/api',methods=['GET'])
# @app.route('/')
def matchingtext():
    d={}
    # inputcv= fileinput.input(files='Nimra Amjad CV.pdf')
    # inputjob= fileinput.input(files='Job.pdf') 

    inputcv=str(request.args['querycv'])
    inputjob=str(request.args['queryjob'])

    # inputcv=request.files['querycv']
    # inputjob=request.files['queryjob']

    # pdf = 'Nimra Amjad Resume.pdf'
    # word = 'Nimra Amjad Resume.docx'
    # cv=Converter(inputcv)
    # cv.convert(inputcv)

    # pdf1 = 'Job.pdf'
    # word1 = 'Job.docx'
    # cv=Converter(inputjob)
    # cv.convert(inputjob)

    # resume = docx2txt.process(word)
    # print(resume)

    # resume = docx2txt.process(inputcv)
    # job_description = docx2txt.process(inputjob)

    # job_description = docx2txt.process(word1)
    # print(job_description)

    text = [inputcv, inputjob]
    # text = [resume, job_description]

    cv = CountVectorizer()
    count_matrix = cv.fit_transform(text)
    # print("\nSimilarity Scores:")
    # print(cosine_similarity(count_matrix))
    matchpercentagee = cosine_similarity(count_matrix)[0][1]*100
    matchpercentage = round(matchpercentagee, 2) #round to two decimals
    # print("your resume matches about " + str(matchpercentage)+ "% of job description.")


    answer=str(matchpercentage)
    d['matching percent']=answer
    return d
    


# def returnascii():
#     d={}
#     inputchr=str(request.args['query'])
#     answer=str(ord(inputchr))
#     d['output']=answer
#     return d
    
if __name__=="__main__":
    app.run()