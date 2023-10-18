import os
import openai


class FineTuner:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    @staticmethod
    def fine_tune(self, type):
        openai.File.create(
            file=open("mydata.jsonl", "rb"),
            purpose='fine-tune'
        )
        openai.FineTuningJob.create(training_file="file-abc123", model="gpt-3.5-turbo")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
