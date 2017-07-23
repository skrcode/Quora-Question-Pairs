#!/bin/bash

# Convert Questions to Sentence Vectors using fastText
FASTTEXT=/Users/16521/Desktop/nlpproj/fastText/fastText
SENTENCE=../data/sentences
TRAINQ1=$SENTENCE/train_question1
TRAINQ2=$SENTENCE/train_question2
TESTQ1=$SENTENCE/test_question1
TESTQ2=$SENTENCE/test_question2
TRAINQ1WV=$SENTENCE/train_question1_wordvecs
TRAINQ2WV=$SENTENCE/train_question2_wordvecs
TESTQ1WV=$SENTENCE/test_question1_wordvecs
TESTQ2WV=$SENTENCE/test_question2_wordvecs
MODEL=../models/model.bin

echo "Getting Train Question 1 Word Vectors..."
$FASTTEXT print-sentence-vectors $MODEL < $TRAINQ1 > $TRAINQ1WV
echo "Got Train Question 1 Word Vectors !"

echo "Getting Train Question 2 Word Vectors..."
$FASTTEXT print-sentence-vectors $MODEL < $TRAINQ2 > $TRAINQ2WV
echo "Got Train Question 2 Word Vectors !"

echo "Getting Test Question 1 Word Vectors..."
$FASTTEXT print-sentence-vectors $MODEL < $TESTQ1 > $TESTQ1WV
echo "Got Test Question 1 Word Vectors !"

echo "Getting Test Question 2 Word Vectors..."
$FASTTEXT print-sentence-vectors $MODEL < $TESTQ2 > $TESTQ2WV
echo "Got Test Question 2 Word Vectors !"

