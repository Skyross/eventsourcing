from eventsourcing.application.simple import SimpleApplication
from eventsourcing.domain.model.events import assert_event_handlers_empty
from eventsourcing.tests.core_tests.test_aggregate_root import ExampleAggregateRoot
from eventsourcing.tests.datastore_tests.test_sqlalchemy import SQLAlchemyDatastoreTestCase


class TestSimpleApplication(SQLAlchemyDatastoreTestCase):
    def tearDown(self):
        # Check the close() method leaves everything unsubscribed.
        assert_event_handlers_empty()

    def test(self):
        with SimpleApplication() as app:
            # Check the application's persistence policy,
            # repository, and event store, are working.
            aggregate = ExampleAggregateRoot.create()
            aggregate.save()
            self.assertTrue(aggregate.id in app.repository)
