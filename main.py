import os
import openai


class FineTuner:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    @staticmethod
    def fine_tune(self, model_type):
        match model_type:
            case "wvw":
                file_name = "./gw2_gpt_training/training_data/gw2_wvw_training.jsonl"

        openai.File.create(
            file=open(file_name, "rb"),
            purpose='fine-tune'
        )
        openai.FineTuningJob.create(training_file="file-abc123", model="gpt-3.5-turbo")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    verify_type = True
    while verify_type:
        model_type = input(">> Model Type:")
        if model_type not in ["wvw"]:
            print("Invalid Model Type.")
        else:
            FineTuner().fine_tune(model_type)
            verify_type = False
