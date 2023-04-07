import openai
import pandas as pd
import pandasql as ps
import time

messages = []
    
openai.api_key = "<YOUR_OPEN_AI_APIk_KEY>"
df_input = pd.read_csv('example.csv')
#user_prompt = "write a sql query to get the the count of activities for each user and sort by descending count"
user_prompt = "write a sql query to get the users who have activity related to AWS along with activity"

def ask_chatgpt(df_input,user_prompt):
    ai_model = "gpt-3.5-turbo"
    #ai_model = "gpt-3.5-turbo-0301"
    #ai_model = "davinci"
    system_msg = "sql"
    messages.append({"role": "system", "content": system_msg})
    messages.append({"role": "user", "content": "Hello"})
    print("Step1 Completed")
    
    df_query = df_input
    table_string = "i have a table with " + str(len(df_query.columns)) + " columns. Columns names are "
    for col in df_query.columns:
        table_string = table_string + col + ", "
    
    messages.append({"role": "user", "content": table_string})
    messages.append({"role": "assistant", "content": "Okay, what would you like to do with this table? Does it need to be modified, queried, or something else?"})
    print("Step2 Completed")
    time.sleep(2)
    
    messages.append({"role": "user", "content": user_prompt})
    response = openai.ChatCompletion.create(
    model=ai_model,
    messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("Step3 Completed")
    time.sleep(2)
    print(reply)
    sql_str = ""
    if reply.find('SELECT') > 0:
        sql_str = reply[reply.find('SELECT'):reply.find('Replace')-6]
        sql_str = sql_str.replace('\n',' ')
        sql_str = sql_str.replace(sql_str.split(" ")[sql_str.split(" ").index('FROM')+1],'df_query')
        print(sql_str)
    
    return ps.sqldf(sql_str)
  
result = ask_chatgpt(df_input,user_prompt)
print(result)
