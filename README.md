
## Installation on tutor:

### app installation:

`cd .local/share/tutor/env/build/openedx/requirements   `

`git clone -b digit-extra https://github.com/NTNUbeta/custom-form-app `

`echo "-e ./custom-form-app" >>  private.txt `

`pip3 install -e custom-form-app `

`tutor images build openedx  `


### plugin activation:

`tutor plugins printroot  `

`mkdir "$(tutor plugins printroot)" `

`cd "$(tutor plugins printroot)" `

`nano minplugin.yml ` den copy all cods from minplugin.yml and saved

`tutor plugins list `

`tutor plugins enable minplugin `

`tutor config save `

`tutor local quickstart `

### Debug:

`tutor local run lms bash `

`./manage.py lms makemigrations `

`./manage.py lms migrate `

###     To be continued .....
