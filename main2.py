import openai
openai.api_key = "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"

engines = openai.Engine.list()
print(engines)
