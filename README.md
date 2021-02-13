# tistory_blog_project
## 첫 번째 프로젝트 블로그 만들기

#### main_page
![main]((https://user-images.githubusercontent.com/67581495/107843560-86333600-6e0f-11eb-94e9-509b4d7d277d.JPG))

#### add login function
![login](https://user-images.githubusercontent.com/67581495/107843727-c1823480-6e10-11eb-9fac-8ce5ed97fcff.JPG)
#### add logout function
```python
def Logout(request):
    if 'user' in request.session:
        del(request.session['user'])
    return redirect('/')
```
#### add register function
![register](https://user-images.githubusercontent.com/67581495/107843730-c515bb80-6e10-11eb-8c3b-345778284abc.JPG)

#### add POST function
![POST](https://user-images.githubusercontent.com/67581495/107843728-c34bf800-6e10-11eb-8310-317ca853ea9a.JPG)
#### add dectators.py required_login
```python
from django.shortcuts import redirect

def login_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None:
            return redirect('/user/login')
        return function(request, *args, **kwargs)
    return wrap
```
#### add comment function
![comment](https://user-images.githubusercontent.com/67581495/107843561-87646300-6e0f-11eb-827e-3d91e431c6c4.JPG)

#### add share to SNS function
![SNS](https://user-images.githubusercontent.com/67581495/107843731-c6df7f00-6e10-11eb-83cf-b86ce09488a3.JPG)
#### add tagging function
![TAG](https://user-images.githubusercontent.com/67581495/107843732-c810ac00-6e10-11eb-85e1-188e9e458b8a.JPG)


