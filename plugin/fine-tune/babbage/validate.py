import os
import openai

openai.api_key = os.getenv("OPEN_API_KEY")


def gpt3_classifier(item, fine_tuned_model, is_log=False):
    # get the reuslt:
    # max token = 1 because to predict one class
    result = openai.Completion.create(model=fine_tuned_model,
                                      prompt=str(item),
                                      max_tokens=50, temperature=0.5,
                                      top_p=1, frequency_penalty=0, presence_penalty=0)
    print(result)
    #if is_log: print('- ', item, ': ', result)

    return result


# this character --> used in the training to indicate end of input
# input_text = "ඒ නිසා මේ නිවාඩුව ලැබුණු ගමන් ම අපි ගමනට පිටත් වෙමු."
input_text = "හිවලා අතින් කට මුවා කර ගෙන සිනා සෙන්නට විය."
# fine_tuned_model = 'ada:ft-msc-research-2022-08-09-21-10-56'
fine_tuned_model = 'babbage:ft-msc-research-2022-08-09-21-39-10'
response = gpt3_classifier(input_text + ' -->', fine_tuned_model)
print(response)
