---
title: Extract Data from Video Files
---


Druid can process video files to extract data from video content, making it searchable and usable within your knowledge base.

{% hint style="info" %}
**NOTE:** This is a tenant feature and requires **Druid Knowledge Base Multimedia Extractor** activation on your tenant. For activation, reach out to your Druid representative.
{% endhint %}

{% hint style="warning" %}
**IMPORTANT!** Extracting data from video files will incur additional costs.
{% endhint %}

Druid supports data extraction (video transcript) from video files only for the following sources:

* SharePoint
* Custom Data Sources
* File repository
* Shared drive
* Website: Videos must be hosted directly on the website. Extraction is not supported for videos embedded from third-party platforms (e.g., YouTube, Vimeo).

## How it works

The process of extracting data from video files involves several automated steps:

1. **Discovery**. During the crawling process, the Knowledge Base (KB) Agent identifies and discovers video files.
2. **Video to Audio Conversion**. Druid utilizes a robust multimedia framework to convert the video file into an audio format (MP4).
3. **Audio Transcription (ASR)**. Automatic Speech Recognition (ASR) technology is then applied to generate a transcript from the audio. This transcript is temporarily stored within Druid. You can download the transcript file from the data source.

![](<../../.gitbook/assets/video download.png>)

4. **Data Extraction**. The KB Agent extracts relevant data from the generated transcript. This is performed using the extractor configured under **Knowledge Base Settings** > **Advanced** > **File Extractors** > **Video**. The default extractor is Druid Standard extractor and Basic content chunker. You can select the LLM content chunker based on your preferences for enhanced extraction.

## Important considerations and limitations

Please be aware of the following when extracting data from video files:

* **Video File Size Limits**: Druid can extract data only from video files with a maximum size of 1GB or an audio duration of 2 hours, whichever is exceeded first. If either of these limits is surpassed, the video file extraction will fail.
* **Processing Time**: Extracting data from larger video files can be a time-consuming process and may take up to several hours to complete.
* **Original Video File Access**: You cannot download the original video file directly from the data source after extraction.
