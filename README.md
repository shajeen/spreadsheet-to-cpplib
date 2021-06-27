<!-- ![spread](https://user-images.githubusercontent.com/2623563/123515225-0f0e8800-d6b4-11eb-99e9-d01b6685e2a8.png) -->

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/shajeen/spreadsheet-to-cpplib/blob/main/README.md">
    <img src="https://user-images.githubusercontent.com/2623563/123515225-0f0e8800-d6b4-11eb-99e9-d01b6685e2a8.png" alt="Logo" width="640" height="320">
  </a>

  <h3 align="center">SpreadSheet-to-cpplib</h3>

  <p align="center">
    An awesome tool to help in your projects!
    <br />
    <a href="https://github.com/shajeen/spreadsheet-to-cpplib/wiki"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/shajeen/spreadsheet-to-cpplib/issues/new?assignees=shajeen&labels=bug&template=bug_report.md&title=">Report Bug</a>
    ·
    <a href="https://github.com/shajeen/spreadsheet-to-cpplib/issues/new?assignees=shajeen&labels=enhancement&template=feature_request.md&title=">Request Feature</a>
  </p>
</p>


## About The Project
![1](https://user-images.githubusercontent.com/2623563/123547683-5a419d00-d77f-11eb-851d-cb4af8273df9.PNG)

There are many great tools available on GitHub, however, I didn't find one that really suit my needs so I created this enhanced one. I want to create a tool which make me a CMake lib and also it does compiles.

## Getting Started

Follow the instructions to setting up project locally.
To get a local copy up and running follow these steps.

### Installation

 Install from the git repo
   ```sh
   pip install https://github.com/shajeen/spreadsheet-to-cpplib.git
   ```
 
 Install from pypi 
   ```sh
   pip install spreadSheet-to-cpplib
   ```
   more information at https://pypi.org/project/spreadSheet-to-cpplib/
  
### How it works

Just pass file name as input argument, and tool will be promoting couple of question. Just answer **yes** or **no**, rest script take care everything. You may find generated files in output folder.

**example of xlsm**
```sh
spreadsheet-to-cpplib --file="Download-Sample-File-xlsm.xlsm"
```

**example of csv**
```sh
spreadsheet-to-cpplib --file="Download-Sample-File.csv"
```

#### Question that tool promots:

<div class="faq-entry">
  <div class="faq-entry-question"><b>Q::(1) Do you want Mathametical Expression library support for formula calculation ?</b></div>
  <div class="faq-entry-answer">:      If you want C++ Mathematical Expression Toolkit header only library. Then please answer **yes** else **no**.</p></div>
  <div class="faq-entry-question">Q::(2) Configure as header-only library ?</div>
  <div class="faq-entry-answer">:      If you want generated output as header-only. Then please answer **yes** else **no**.</p></div>
  <div class="faq-entry-question">Q::(3) Get default value from formula as double.?</div>
  <div class="faq-entry-answer">:      If you want Formaul to be present as string in generated output. Then please answer **yes** else **no**.</p></div>
  <div class="faq-entry-question">Q::(4) Make string as 0.0?</div>
  <div class="faq-entry-answer">:      If you want any string as zero in generated output. Then please answer **yes** else **no**.</p></div>
</div>

## Working Screenshot
![2](https://user-images.githubusercontent.com/2623563/123547680-59107000-d77f-11eb-8cb1-d05e8e8b9932.PNG)

## Roadmap

See the [open issues](https://github.com/shajeen/spreadsheet-to-cpplib/issues) for a list of proposed features (and known issues).

### Contributing

Any contributions you make are **greatly appreciated**.

1. Create an issue describing your changes.
2. Fork the repo, make the changes and please dont forget to test.
3. Create the pull request. 

Please read the [CONTRIBUTING](https://github.com/shajeen/spreadsheet-to-cpplib/blob/main/CONTRIBUTING.md) before raising the PR.

## License

Distributed under the GPL-3.0 License. See `LICENSE` for more information.

## Contact

 - Shajeen Ahamed - [@shajeenahamed](https://twitter.com/shajeenahamed) - shajeenahmed@gmail.com
 - Project Link: [https://github.com/shajeen/spreadsheet-to-cpplib](https://github.com/shajeen/spreadsheet-to-cpplib)

