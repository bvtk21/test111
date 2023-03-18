import openai
openai.api_key = "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"

engines = openai.Engine.list()
print(engines)
