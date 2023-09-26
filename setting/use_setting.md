[vscode](#vscode)
[pycham](#pycham)
- 파이썬 공식문서: https://abit.ly/pb-document
## vscode

### 기본 설정

- 단축키 지정: >preferences: open keyboard shortcuts/바로가기키(검색창) -> Python run, Python debug
- 마우스 휠 조정: file>preference>setting> mouse검색
- Json 설정: > Preferences: Open User Settings(Json)
```
{
    "workbench.colorTheme": "Default Dark Modern",
    "editor.fontSize": 20,
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
    "terminal.integrated.enableMultiLinePasteWarning": false,
    "typescript.locale": "ko",
    "workbench.settings.applyToAllProfiles": [
        "typescript.locale"
    ]

}
```


### 확장자
- 한글설정: Korean Language Pack for Visual Studio code 
- python관련(6): Bracket pair color dlw / indent-rainbow / Live Server / Markdown All in One / Python / vscode-icons
- 쥬피터: Jupyter / 
- 장고 및 웹(4): Django / SQlite / Auto Rename Tag / Highlight Matching Tag 


## pycham

### 기본 설정
- 오른쪽 상단(실행 버튼 옆): Edit-configuration
- 마우스 설정: Setting>mouse검색>general(일반)
- 단축키 등록: Setting>keymap> Run, Debug검색
### 확장자(Plugin)
- 한글설정: Korean Language Pack
- Vscode Keymap / Markdown
- rainbow brackets / indent rainbow
