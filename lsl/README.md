# EEG Collection modules
Streaming EEG data using Lab Streaming Layer, ping markers through LSL for synchronisation, and post-processing of EEG data of such data

## Dependencies
- `requirements.txt` of all python modules (I don't really know how to use conda)
- [LabRecorder](https://github.com/labstreaminglayer/App-LabRecorder) is used to record the data to `.xdf` file formats, this is optional
  
## Markers
The `marker_stream` module creates a LSL 

## Emotiv EPOC+ Headset
The collection of EEG data is achieved using the Emotiv EPOC+ headset provided by the Monash University. The following links are rerefence manual
for the headset and EmotivPRO lab software

- [EPOC+ Headset](https://emotiv.gitbook.io/epoc-user-manual/)
- [EmotivPRO software](https://emotiv.gitbook.io/emotivpro-v3/)

The [CSV file headers references](https://emotiv.gitbook.io/emotivpro-v3/managing-your-eeg-data-recordings/exporting-an-eeg-data-recording/csv-files) will be useful for the development of the post-processing script after EEG data collection

## pylsl
Python's interface for LSL
https://github.com/labstreaminglayer/liblsl-Python