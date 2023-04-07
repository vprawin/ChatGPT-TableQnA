# ChatGPT-TableQnA
Table Question and Answering leveraged on ChatGPT

ChatGPT, a large language model developed by OpenAI based on the GPT (Generative Pre-trained Transformer) architecture. ChatGPT has been trained on a massive amount of data, and the goal is to generate human-like responses to text-based inputs. ChatGPT can answer a wide variety of questions and engage in natural language conversations on a range of topics.

TAPAS (Task Adaption for Parsimonious Attention) is a type of transformer-based neural network architecture that is designed to perform better on natural language processing (NLP) tasks that require reasoning and inference over structured information, such as tables. TAPAS is a modification of the BERT (Bidirectional Encoder Representations from Transformers) architecture, which is one of the most widely used NLP models.

TAPAS was introduced in a research paper by Google AI in 2020 and has since been used for various NLP tasks such as question-answering, text classification, and entity recognition. One of the unique features of TAPAS is its ability to efficiently process tabular data while still being able to leverage the pre-training and transfer learning capabilities of the BERT architecture.

ChatGPT4 is currently not capable of uploading Data and Responsding to queries based on the data. Hence we are leveraging the ChatGPT's sequential questioning capabilities to train it to understand the table struncture and respond back with SQL Queries. Later SQL is used to Query Data and respond back to user

Note:
  1. OpenAI Python Libraries are limited to ChatGPT-3.5 model and only selected users are allowed to use ChatGPT-4
  2. ChatGPT-4 Preview is limited only to UI
  3. Currently ChatGPT-3.5 / ChatGPT-3.5 Turbo is used and response time is slightly higher than ChatGPT-4 (Tested manually using UI)
  
Python Libraries Required
  1. OpenAI
  2. Pandas
  3. PandasSQL
