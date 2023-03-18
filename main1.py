import openai
openai.api_key = "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"

engines = openai.Engine.list()
print(engines)
