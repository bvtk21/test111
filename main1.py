import openai
openai.api_key = "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"

engines = openai.Engine.list()
print(engines)
