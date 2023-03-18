import openai
openai.api_key = "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"

engines = openai.Engine.list()
print(engines)
