import os
import openai
from dotenv import load_dotenv

load_dotenv()


class FineTuner:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    @staticmethod
    def fine_tune(model_type):
        match model_type:
            case "wvw":
                file_name = "gw2_gpt_training/training_data/gw2_wvw_training.jsonl"
        print("Creating training file...")
        training_file = openai.File.create(
            file=open(file_name, "rb"),
            purpose='fine-tune'
        )
        print(f"Training file created: {training_file['id']}")
        print("Creating Fine Tuning job...")
        openai.FineTuningJob.create(training_file=training_file["id"], model="gpt-3.5-turbo")
        print("Done!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    verify_type = True
    while verify_type:
        print(f"Available Options: [wvw]")
        model_type = input(">> Model Type: ")
        if model_type not in ["wvw"]:
            print("Invalid Model Type.")
        else:
            FineTuner().fine_tune(model_type)
            verify_type = False
