from __future__ import print_function
import pytest

@pytest.fixture(scope='module') # use decorator to specify `resource_a_setup` as a pytest.fixture
# defined it in module scope so if two tests need it it will only have one setup and teardown functions
def resource_a_setup(request): # we need a a request parameter to do all this
    print('\nresources_a_setup()')
    def resource_a_teardown(): # specify `resource_a_teardown()` as a finalizer for `resource_a_setup()`
        print('\nresources_a_teardown()')
    request.addfinalizer(resource_a_teardown)

def test_1_that_needs_resource_a(resource_a_setup):
    print('test_1_that_needs_resource_a()')

def test_2_that_does_not():
    print('\ntest_2_that_does_not()')

def test_3_that_does(resource_a_setup):
    print('\ntest_3_that_does()')

# Major benefits of PYTEST

'''
It’s obvious which tests are using a resource, as the resource is listed in the test param list.
I don’t have to artificially create classes (or move tests from one file to another) just to separate fixture usage.
The teardown code is tightly coupled with the setup code for one resource.
Scope for the lifetime of the resource is specified at the location of the resource setup code. This ends up being a huge benefit when you want to fiddle with scope to save time on testing. If everything starts going haywire, it’s a one line change to specify function scope, and have setup/teardown run around every function/method.
It’s less code. The pytest solution is smaller than the class solution
'''


















