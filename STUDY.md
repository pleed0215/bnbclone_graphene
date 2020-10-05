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
