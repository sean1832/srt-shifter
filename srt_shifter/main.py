import argparse
import json
from datetime import datetime, timedelta


def shift_srt_time(srt_file_path, shift_seconds, output_file_path):
    time_format = "%H:%M:%S,%f"
    shift_delta = timedelta(seconds=shift_seconds)

    with open(srt_file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open(output_file_path, "w", encoding="utf-8") as file:
        for line in lines:
            if "-->" in line:
                start_time_str, end_time_str = line.split(" --> ")
                start_time = (
                    datetime.strptime(start_time_str, time_format) + shift_delta
                )
                end_time = (
                    datetime.strptime(end_time_str.strip(), time_format) + shift_delta
                )
                line = (
                    start_time.strftime(time_format)[:-3]
                    + " --> "
                    + end_time.strftime(time_format)[:-3]
                    + "\n"
                )
            file.write(line)


def get_parser():
    parser = argparse.ArgumentParser(description="Shift srt subtitle time",)
    parser.add_argument("input_path", type=str, help="Path to srt file")
    parser.add_argument("shift_seconds", type=float, help="Shift time in seconds")
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Path to output file, default replace original file",
    )

    version = json.load(open("srt_shifter/meta.json", "r"))["version"]
    parser.add_argument("-v", "--version", action="version", version=f"{version}")
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()

    srt_file_path = args.input_path
    shift_seconds = args.shift_seconds
    output_file_path = args.output

    if not srt_file_path:
        raise ValueError("Input file path is required")
    if shift_seconds is None:
        raise ValueError("Shift seconds is required")
    if shift_seconds == 0:
        print("Shift seconds is 0, no change")
        return
    if not srt_file_path.endswith(".srt"):
        raise ValueError("Input file must be srt file")

    if output_file_path is None:
        output_file_path = srt_file_path
    shift_srt_time(srt_file_path, shift_seconds, output_file_path)


if __name__ == "__main__":
    main()
