from unittest import TestCase

from app import create_app


mock_data = {
 "cutoffValue": 0.5,
 "referralUserIdValue": 0.25,
 "baseMutualContactsValue": 0.05,
 "baseMutualEventsValue": 0.05,
 "baseMutualCirclesValue": 0.05,
 "userId": "6740ebce66212d34d741d0e3",
     "referralUserID": "67aa5510e6abc0eecdc37a7b",
 "prompt": "Paris, France, Music Producer / Collective Founder / Co-Head of Recod Label, Showcase work or portfolio, Receive jobs / hirings, Grow audience / business, Find collaborators, Exchange with other creators, Connect with mentors / advisors, Build partnerships, Entrepreneurship, Cultural exchange, Content Creation, Art, Lithuania, Hamburg, Ghent, Dubai, Delhi, Cologne, Buenos Aires, Belgium, Barcelona, Australia, Argentina, Antwerp, Amsterdam, Abu Dhabi",
 "exclude": [
  "67fd2e491d937d205e8d731e",
  "67aa5510e6abc0eecdc37a164",
 ],
 "contacts": [
   "6740edc266212d34d741dea6",
   "6751c17dc358b1f74871e80b",
   "6755fe755aca1a4ca42caa8b",
 ],
 "circles": [
   "67b46139a38358de8bf56e7b",
 ],
 "events": [
   "684b446166924406820338e3"
 ]
}


class TestRoutes(TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_recommended_users_response(self):
        with self.app.app_context():
            response = self.client.post('/recommended_users', json=mock_data, headers={'Authorization': 'Bearer test'})
            self.assertEqual(response.status_code, 200)
            json = response.json
            assert json == mock_data
