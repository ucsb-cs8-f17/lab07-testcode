#!/usr/bin/env python3
import pytest
import os
from lab07 import createWordList

def test_createWordList_0():
  lwords = ['apple', 'banana', 'orange']
  outfile = open('test_file_0.txt', 'w')
  for elem in lwords:
    outfile.write(elem +'\n')

  outfile.close()
  newlist = createWordList('test_file_0.txt')

  print(len(newlist) , len(lwords))
  assert(len(newlist) ==len(lwords))
  
  for i in range(len(lwords)):
    assert(lwords[i]==newlist[i])

def test_createWordList_1():
  try:
    createWordList('someNon-ExistantFile.txt')
    assert(False)
  except FileNotFoundError as e:
    print(str(e))

from lab07 import canWeMakeIt

def test_canWeMakeIt_0():
  assert(canWeMakeIt('ape','pae') == True)

def test_canWeMakeIt_1():
  assert(canWeMakeIt('ape','paels') == True)

def test_canWeMakeIt_2():
  assert(canWeMakeIt('ape','pel') == False)

def test_canWeMakeIt_3():
  assert(canWeMakeIt('ape','') == False)

def test_canWeMakeIt_4():
  assert(canWeMakeIt('apple','pel') == False)

def test_canWeMakeIt_5():
  assert(canWeMakeIt('lion','iolln') == True)

from lab07 import getWordPoints
letterPoints = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4,\
                  'g':2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1,\
                  'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1,\
                  's':1, 't':1, 'u':1, 'v':4,  'w':4, 'x':8,\
                  'y':4, 'z':10}

def test_getWordPoints_0():
  assert(getWordPoints('ape',letterPoints) == 5)

def test_getWordPoints_1():
  assert(getWordPoints('nape',letterPoints) == 6)

def test_getWordPoints_2():
  assert(getWordPoints('pan',letterPoints) == 5)

def test_getWordPoints_3():
  assert(getWordPoints('goin\'',letterPoints) == 2+1+1+1)

def test_getWordPoints_4():
  emptyDict = {}
  assert(getWordPoints('goin\'',emptyDict) == 0)

from lab07 import outputWordPointPairs, getWordPoints


def test_outputWordPointPairs_0():
  # This case prints to standard output
  pointWordList = [(6, 'ape'),]
  outputWordPointPairs(pointWordList, 'eap', False)
  

def test_outputWordPointPairs_1():
  words = ['ape', 'nape', 'pipe', 'pan','goin\'' ]
  pointWordList = []
  for w in words:
    pointWordList.append((getWordPoints(w, letterPoints), w))

  outputWordPointPairs(pointWordList, 'apenpigon\'', False)

def test_outputWordPointPairs_2():
  # Write to file
  words = ['ape', 'nape', 'pipe', 'pan','go' ]
  pointWordList = []
  for w in words:
    pointWordList.append((getWordPoints(w, letterPoints), w))

  outputWordPointPairs(pointWordList, 'apenpigon', True)
  try:
    f = open('apenpigon.txt')
    line = f.readline()
    count = 0
    
    while line:
      line = line.strip()
      wordPoints=line.split()
      if (wordPoints[0] not in words) or \
         int(wordPoints[1])!= getWordPoints(wordPoints[0], letterPoints):
        assert(False)
      count = count +1
      line = f.readline()
      
    if count != len(words):
      assert(False)
    f.close()
  except:
    assert(False)

def createWordPointDict(filename):
  s= open(filename)
  wordPointDict ={}
  sline = s.readline()
  while sline:
      sline = sline.strip()
      slst = sline.split()
      wordPointDict[slst[0]]=int(slst[1])
      sline = s.readline()
  s.close()
  return wordPointDict

def createPointList(filename):
  s= open(filename)
  pointList =[]
  sline = s.readline()
  while sline:
      sline = sline.strip()
      slst = sline.split()
      pointList.append(int(slst[1]))
      sline = s.readline()
  s.close()
  return pointList



def checkNumWords(testnum, letters): 
  try:
    studentFile = letters+'.txt'
    studentWordPoints = createWordPointDict(studentFile) # open the file generated by the student  
  except:
    sys.stderr.write('Could not open student file'+ studentFile+'\n')
    assert(False)
  try:
    instructorFile= 'scrabbleWords_test_'+str(testnum)+'.txt'
    instructorWordPoints = createWordPointDict(instructorFile) #open the instructor file 
  except:
    sys.stderr.write('Could not open instructor file'+ instructorFile+'\n')
    assert(False)
    
  if len(studentWordPoints) != len(instructorWordPoints):
    sys.stderr.write('Number of words in each file is different')
    assert(False)

     
def test_scrabbleWords_0():
  os.system('./lab07.py diba')
  checkNumWords(0,'diba')

def test_scrabbleWords_1():
  os.system('./lab07.py mouse')
  checkNumWords(1, 'mouse')
 
def test_scrabbleWords_2():
  #Check that all the words and point values the student found are correct
  os.system('./lab07.py coward')
  studentWordPoints = createWordPointDict('coward.txt') # open the file generated by the student  
  instructorWordPoints = createWordPointDict('scrabbleWords_test_2.txt') #open the instructor file 
  keys=studentWordPoints.keys()
  for key in keys:
    if studentWordPoints[key]!=instructorWordPoints.get(key,0):
      assert(False)
  
def test_scrabbleWords_3():
  #Check that the students point values are in descending order
  os.system('./lab07.py mouse')
  studentPoints = createPointList('mouse.txt') # open the file generated by the student  
  for i in range(len(studentPoints)-1):
    if studentPoints[i]<studentPoints[i+1]:
      assert(False)
      
from lab07 import scrabbleWords

def test_scrabbleWords_4():
  #Check that all the words and point values the student found are correct
  scrabbleWords('coward')
  studentWordPoints = createWordPointDict('coward.txt') # open the file generated by the student  
  instructorWordPoints = createWordPointDict('scrabbleWords_test_2.txt') #open the instructor file 
  keys=studentWordPoints.keys()
  for key in keys:
    if studentWordPoints[key]!=instructorWordPoints.get(key,0):
      assert(False)
  
