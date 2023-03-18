import openai
openai.api_key = "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"

engines = openai.Engine.list()
print(engines)
