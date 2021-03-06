# 4 GRAPHQL INTRO

## 4.3 Graphene Setup

- 일단 여기까지는 nicolas가 제공한 blueprint를 이용하였음.

  - graphene과 django연결은 graphene-django를 사용하면 된다함.
    - pipenv install graphene-django 후에 꼭 settings.py에 가서 apps를 추가해주자.
    - 그리고 urls에 가서 graphql url을 추가해주자.

- Query, Mutation, Schema가 필요하다.

  - Query에는 field와 resolver가 필요하다.

    ```python
      # Query는 graphene의 ObjectType을 상속 받아야 한다.
      class Query(graphene.ObjectType):
        hello = graphene.String()

        def resolve_hello(self, info):
          pass
    ```

    - 이런 식으로 Query를 만들어주면 된다.
    - info는 resolver의 정보를 담은 객체.
      - info.context는 request와 비슷한 역할임.
        - info.context.user하면 user정보가 나옴.

# 5 GraphQL Api

## 5.1 Pagination

- field 정의에서 일르테면 List에 page 옵션을 주고 싶으면, page=graphene.Int() 식으로, kwargs를 추가해주면 된다.
- RoomListResponse ???
  - 이런식으로 처리해주는게 더 좋다고 하는데, list와 total을 가지고 있는 오브젝트.
  - 코드 참고를 하자~! 이렇게 해주는 방식이 더 좋다고 하는뎅..
- RoomDetail
  - id 입력을 필수로 해야하게 하고 싶으면, required=True 를 주면 된다.

## 5.3 Create Account

- Query와 Mutation 차이
  - Query는 데이터 조회, Mutation은 db 조작.
  - Mutation 클래스 만드는 방법은 코드를 참고.
    - Mutation class는 모두 mutate method(self, info)가 필요하다.
- Query class 안의 resolve도 분리하는 것이 좋다.

## 5.4 Login

- DRF 와는 다른 점
  - jwt 토큰을 encode하면 token 값이 항상 앞에 b'~~~' 이렇게 되어 있는 것을 확인할 수 있는데, 이것의 type을 보면 bytes로 되어 있다.
    - 이 녀석을 docode해줘야 한다. 그래서 token.decode("utf-8")로 토큰값을 넘겨주도록 하자.

## 5.5 JWT Middleware

- Authorization 관련해서 graphql은 Middleware를 만들면 된다.
- middlewares.py를 만들고, 관련 문서도 확인 해보자.
  - django-graphql-jwt 라이브러리가 있지만, 업데이트가 잘 되지 않아 권장하지 않는다고 한다.
- config.settings에 추가할 내용이 있다.
  ```python
    GRAPHENES = {
      'MIDDLEWARE': (
        'path.to.mymiddleware.class',
      )
    }
  ```
  - 이런식으로 authorization middleware를 추가하면 된다.
  - rest api 처럼 header에 로그인 정보를 넘겨서 테스트하고 싶은데, 어떻게 하면될까?
    - Altair 라는 구글 확장프로그램을 사용하면 된다.


## 5.9 Dynamic Fields
- REST API 때와 비슷함. is_favs
  - dynamic field를 추가할 경우에는, resolver를 같이 추가해줘야 한다.
    - resolver의 인수로는 parent, info (parent는 self에 해당하겠지만, print 해보면 해당 object를 리턴해준다.)