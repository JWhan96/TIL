[vscode](#vscode)
[pycham](#pycham)
- 파이썬 공식문서: https://abit.ly/pb-document
## vscode

### 기본 설정

### 확장자
- 한글설정: Korean Language Pack for Visual Studio code
- python관련(6): Bracket pair color dlw / indent-rainbow / Live Server / Markdown All in One / Python / vscode-icons / tabout / Code Runner
- 쥬피터: Jupyter / 
- 장고 및 웹(4): Django / SQlite / Auto Rename Tag / Highlight Matching Tag 
- c++ : c/c++ / 자동으로 추천해주는 c++ extension
- cpp: "cpp": "cd $dir && g++ -std=c++17 $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt < input.txt"
- code runner설정: Ignore Selection 체크, Run In Terminal 체크

- 단축키 지정: >preferences: open keyboard shortcuts/바로가기키(검색창) -> Python run, Python debug
- 마우스 휠 조정: file>preference>setting> mouse검색
- Json 설정: > Preferences: Open User Settings(Json)
```json
{
    "workbench.colorTheme": "Default Dark Modern",
    "editor.fontSize": 14,
    "workbench.iconTheme": "vscode-icons",
    "editor.mouseWheelZoom": true,
    "window.zoomLevel": 1,
    "liveServer.settings.donotShowInfoMsg": true,

    "editor.tabSize": 2,
    // python
    "[python]": {
        "editor.tabSize": 4
    },

    // Django
    "files.associations": {
        "**/*.html": "html",
            "**/templates/**/*.html": "django-html",
        "**/templates/**/*": "django-txt",
        "**/requirements{/**,*}.{txt,in}": "pip-requirements"
    },
    "emmet.includeLanguages": {
        "django-html": "html"
    },
    "terminal.integrated.defaultProfile.windows": "Git Bash",
    "terminal.integrated.enableMultiLinePasteWarning": "never",
    "typescript.locale": "ko",
    "workbench.settings.applyToAllProfiles": [
        "typescript.locale"
    ],
    "code-runner.executorMap": {

        "javascript": "node",
        "java": "cd $dir && javac $fileName && java $fileNameWithoutExt",
        "c": "cd $dir && gcc $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        "zig": "zig run",
        // "cpp": "cd $dir && g++ $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        "cpp": "cd $dir && g++ -std=c++17 $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt < input.txt",
        "objective-c": "cd $dir && gcc -framework Cocoa $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        "php": "php",
        "python": "python -u",
        "perl": "perl",
        "perl6": "perl6",
        "ruby": "ruby",
        "go": "go run",
        "lua": "lua",
        "groovy": "groovy",
        "powershell": "powershell -ExecutionPolicy ByPass -File",
        "bat": "cmd /c",
        "shellscript": "bash",
        "fsharp": "fsi",
        "csharp": "scriptcs",
        "vbscript": "cscript //Nologo",
        "typescript": "ts-node",
        "coffeescript": "coffee",
        "scala": "scala",
        "swift": "swift",
        "julia": "julia",
        "crystal": "crystal",
        "ocaml": "ocaml",
        "r": "Rscript",
        "applescript": "osascript",
        "clojure": "lein exec",
        "haxe": "haxe --cwd $dirWithoutTrailingSlash --run $fileNameWithoutExt",
        "rust": "cd $dir && rustc $fileName && $dir$fileNameWithoutExt",
        "racket": "racket",
        "scheme": "csi -script",
        "ahk": "autohotkey",
        "autoit": "autoit3",
        "dart": "dart",
        "pascal": "cd $dir && fpc $fileName && $dir$fileNameWithoutExt",
        "d": "cd $dir && dmd $fileName && $dir$fileNameWithoutExt",
        "haskell": "runghc",
        "nim": "nim compile --verbosity:0 --hints:off --run",
        "lisp": "sbcl --script",
        "kit": "kitc --run",
        "v": "v run",
        "sass": "sass --style expanded",
        "scss": "scss --style expanded",
        "less": "cd $dir && lessc $fileName $fileNameWithoutExt.css",
        "FortranFreeForm": "cd $dir && gfortran $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        "fortran-modern": "cd $dir && gfortran $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        "fortran_fixed-form": "cd $dir && gfortran $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        "fortran": "cd $dir && gfortran $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        "sml": "cd $dir && sml $fileName",
        "mojo": "mojo run"
    },
    "code-runner.ignoreSelection": true,
    "code-runner.runInTerminal": true,
    "code-runner.terminalRoot": "/",

}

```




## pycham

### 기본 설정
- 오른쪽 상단(실행 버튼 옆): Edit-configuration
- 마우스 설정: Setting>mouse검색>general(일반)
- 단축키 등록: Setting>keymap> Run, Debug검색
### 확장자(Plugin)
- 한글설정: Korean Language Pack
- Vscode Keymap / Markdown
- rainbow brackets / indent rainbow
