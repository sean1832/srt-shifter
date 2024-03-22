## SRT Time Shifter

A simple python script that shifts the time of a SRT subtitle file by a given amount of seconds.

### Installation

```bash
git clone https://github/sean1832/srt-shifter.git
cd srt-shifter
pip install .
```

### Usage

```bash
srt-shifter <input_file> <shift_seconds> [output_file]
```
---
Example:
```bash
srt-shifter subtitles.srt -5
```

This will shift the subtitles 5 seconds backward and write the result to `subtitles_shifted.srt`.

```bash
srt-shifter subtitles.srt 5 -o shifted_subtitles.srt
```

This will shift the subtitles 5 seconds forward and write the result to `shifted_subtitles.srt`.

### License
[Apache License 2.0](LICENSE)