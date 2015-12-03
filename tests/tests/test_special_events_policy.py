import cloudpassage
import json
import os
import pytest

key_id = os.environ.get('HALO_KEY_ID')
secret_key = os.environ.get('HALO_SECRET_KEY')
bad_key = "abad53c"
api_hostname = os.environ.get('HALO_API_HOSTNAME')
proxy_host = '190.109.164.81'
proxy_port = '1080'


class TestSpecialEventsPolicy:
    def create_special_events_policy_obj(self):
        session = cloudpassage.HaloSession(key_id, secret_key)
        return cloudpassage.SpecialEventsPolicy(session)

    def test_instantiation(self):
        assert self.create_special_events_policy_obj()

    def test_list_all(self):
        session = cloudpassage.HaloSession(key_id, secret_key)
        se_policy = cloudpassage.SpecialEventsPolicy(session)
        se_policy_list = se_policy.list_all()
        assert "id" in se_policy_list[0]

    def test_create(self):
        rejected = False
        policy = self.create_special_events_policy_obj()
        try:
            policy.create("DoesNotEvenMatter")
        except NotImplementedError:
            rejected = True
        assert rejected

    def test_update(self):
        rejected = False
        policy = self.create_special_events_policy_obj()
        try:
            policy.update("DoesNotEvenMatter")
        except NotImplementedError:
            rejected = True
        assert rejected

    def test_describe(self):
        rejected = False
        policy = self.create_special_events_policy_obj()
        try:
            policy.describe("DoesNotEvenMatter")
        except NotImplementedError:
            rejected = True
        assert rejected

    def test_delete(self):
        rejected = False
        policy = self.create_special_events_policy_obj()
        try:
            policy.delete("DoesNotEvenMatter")
        except NotImplementedError:
            rejected = True
        assert rejected
