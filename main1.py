import openai
openai.api_key = "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"

engines = openai.Engine.list()
print(engines)
