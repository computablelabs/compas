from asciimatics.widgets import Layout, Label, Text, Button
from models.ui import UI
from viewmodels.datatrust.detail import Detail as VM
from views.detail import Detail
from widgets.popup import PopUpDialog

class Detail(Detail):
    def __init__(self, screen):
        super(Detail, self).__init__(screen, screen.height, screen.width,
            hover_focus=True, can_scroll = False, title='::Datatrust::', reduce_cpu=True)

        self.check_theme()
        # keep a pointer to the viewmodel so my super methods work correctly
        self.vm = VM()
        self.inject_header()

        main = Layout([11,28,28,28,5], fill_frame=True)
        self.add_layout(main)

        self.inject_get_address_and_owner(main, 5)

        self.inject_register(main)
        self.inject_dividers(main, 5)
        self.inject_resolve_registration(main)
        self.inject_dividers(main, 5)
        self.inject_get_backend_address(main)
        self.inject_dividers(main, 5)
        self.inject_get_backend_url(main)
        self.inject_dividers(main, 5)
        self.inject_set_backend_url(main)
        self.inject_dividers(main, 5)
        self.inject_get_data_hash(main)
        self.inject_dividers(main, 5)
        self.inject_set_data_hash(main)
        self.inject_dividers(main, 5)
        self.inject_get_bytes_purchased(main)
        self.inject_dividers(main, 5)
        self.inject_get_delivery(main)
        self.inject_dividers(main, 5)
        self.inject_request_delivery(main)
        self.inject_dividers(main, 5)
        self.inject_get_access_reward_earned(main)
        self.inject_dividers(main, 5)
        self.inject_listing_accessed(main)
        self.inject_dividers(main, 5)
        self.inject_delivered(main)
        self.inject_dividers(main, 5)
        self.inject_get_hash(main)
        self.inject_dividers(main, 5)
        self.inject_get_reserve(main)
        self.inject_dividers(main, 5)
        self.inject_get_privileged(main)
        self.inject_dividers(main, 5)
        self.inject_set_privileged(main)
        self.inject_dividers(main, 5)

        self.inject_footer()

        self.fix()

    def inject_register(self, layout):
        layout.add_widget(Label('Register'), 0)
        layout.add_widget(Text(label='URL:', name='register_url', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Send', self.register), 4)

    def register(self):
        url = self.data.get('register_url')
        gas_price = self.data.get('gas_price')
        if url and gas_price:
            res = self.vm.register(url, gas_price)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_resolve_registration(self, layout):
        layout.add_widget(Label('Reslove Registration'), 0)
        layout.add_widget(Text(label='Hash:', name='resolve_hash', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Send', self.resolve_registration), 4)

    def resolve_registration(self):
        hash = self.data.get('resolve_hash')
        gas_price = self.data.get('gas_price')
        if hash and gas_price:
            res = self.vm.resolve_registration(hash, gas_price)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_backend_address(self, layout):
        layout.add_widget(Label('Get Backend Address'), 0)
        layout.add_widget(Label(' '), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Call', self.get_backend_address), 4)

    def get_backend_address(self):
        # we'll use the viewmodel to relay commands
        res = self.vm.get_backend_address()
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_backend_url(self, layout):
        layout.add_widget(Label('Get Backend URL'), 0)
        layout.add_widget(Label(' '), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Call', self.get_backend_url), 4)

    def get_backend_url(self):
        # we'll use the viewmodel to relay commands
        res = self.vm.get_backend_url()
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_set_backend_url(self, layout):
        layout.add_widget(Label('Set Backend URL'), 0)
        layout.add_widget(Text(label='URL:', name='set_backend_url', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Send', self.set_backend_url), 4)

    def set_backend_url(self):
        url = self.data.get('set_backend_url')
        gas_price = self.data.get('gas_price')
        if url and gas_price:
            res = self.vm.set_backend_url(url, gas_price)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_data_hash(self, layout):
        layout.add_widget(Label('Get Data Hash'), 0)
        layout.add_widget(Text(label='Listing Hash:', name='get_data_hash_listing', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Call', self.get_data_hash), 4)

    def get_data_hash(self):
        listing = self.data.get('get_data_hash_listing')
        # we'll use the viewmodel to relay commands
        res = self.vm.get_data_hash(listing)
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_set_data_hash(self, layout):
        layout.add_widget(Label('Set Data Hash'), 0)
        layout.add_widget(Text(label='Listing Hash:', name='set_data_hash_listing', on_change=self.on_changed), 1)
        layout.add_widget(Text(label='Data Hash:', name='set_data_hash_data', on_change=self.on_changed), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Send', self.set_data_hash), 4)

    def set_data_hash(self):
        listing = self.data.get('set_data_hash_listing')
        data = self.data.get('set_data_hash_data')
        gas_price = self.data.get('gas_price')
        if listing and data and gas_price:
            res = self.vm.set_data_hash(listing, data, gas_price)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_bytes_purchased(self, layout):
        layout.add_widget(Label('Get Bytes Purchased'), 0)
        layout.add_widget(Text(label='Address:', name='get_bytes_purchased_addr', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Call', self.get_bytes_purchased), 4)

    def get_bytes_purchased(self):
        addr = self.data.get('get_bytes_purchased_addr')
        # we'll use the viewmodel to relay commands
        res = self.vm.get_bytes_purchased(addr)
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_delivery(self, layout):
        layout.add_widget(Label('Get delivery'), 0)
        layout.add_widget(Text(label='Hash:', name='get_delivery_hash', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Call', self.get_delivery), 4)

    def get_delivery(self):
        hash = self.data.get('get_delivery_hash')
        res = self.vm.get_delivery(hash)
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_request_delivery(self, layout):
        layout.add_widget(Label('Request Delivery'), 0)
        layout.add_widget(Text(label='Hash:', name='request_delivery_hash', on_change=self.on_changed), 1)
        layout.add_widget(Text(label='Amount:', name='request_delivery_amount', on_change=self.on_changed), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Send', self.request_delivery), 4)

    def request_delivery(self):
        hash = self.data.get('request_delivery_hash')
        amount = self.data.get('request_delivery_amount')
        gas_price = self.data.get('gas_price')
        if hash and amount and gas_price:
            res = self.vm.request_delivery(hash, amount, gas_price)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_access_reward_earned(self, layout):
        layout.add_widget(Label('Get Access Reward'), 0)
        layout.add_widget(Text(label='Listing Hash:', name='get_access_reward_hash', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Call', self.get_access_reward_earned), 4)

    def get_access_reward_earned(self):
        hash = self.data.get('get_access_reward_hash')
        res = self.vm.get_access_reward_earned(hash)
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_listing_accessed(self, layout):
        layout.add_widget(Label('Listing Accessed'), 0)
        layout.add_widget(Text(label='Listing Hash:', name='listing_accessed_listing', on_change=self.on_changed), 1)
        layout.add_widget(Text(label='Delivery Hash:', name='listing_accessed_delivery', on_change=self.on_changed), 2)
        layout.add_widget(Text(label='Amount:', name='listing_accessed_amount', on_change=self.on_changed), 3)
        layout.add_widget(Button('Send', self.listing_accessed), 4)

    def listing_accessed(self):
        listing = self.data.get('listing_accessed_listing')
        delivery = self.data.get('listing_accessed_delivery')
        amount = self.data.get('listing_accessed_amount')
        gas_price = self.data.get('gas_price')
        if listing and delivery and amount and gas_price:
            res = self.vm.listing_accessed(listing, delivery, amount, gas_price)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_delivered(self, layout):
        layout.add_widget(Label('Delivered'), 0)
        layout.add_widget(Text(label='Hash:', name='delivered_hash', on_change=self.on_changed), 1)
        layout.add_widget(Text(label='Amount:', name='delivered_url', on_change=self.on_changed), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Send', self.delivered), 4)

    def delivered(self):
        hash = self.data.get('delivered_hash')
        url = self.data.get('delivered_url')
        gas_price = self.data.get('gas_price')
        if hash and url and gas_price:
            res = self.vm.delivered(hash, url, gas_price)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_hash(self, layout):
        layout.add_widget(Label('Get Hash'), 0)
        layout.add_widget(Text(label='URL:', name='get_hash_url', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Call', self.get_hash), 4)

    def get_hash(self):
        url = self.data.get('get_hash_url')
        res = self.vm.get_hash(url)
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_reserve(self, layout):
        layout.add_widget(Label('Get Reserve'), 0)
        layout.add_widget(Label(' '), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Call', self.get_reserve), 4)

    def get_reserve(self):
        res = self.vm.get_reserve()
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_set_privileged(self, layout):
        layout.add_widget(Label('Set Privileged'), 0)
        layout.add_widget(Text(label='Listing:', name='set_privileged_listing', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Send', self.set_privileged), 4)

    def set_privileged(self):
        listing = self.data.get('set_privileged_listing')
        gas_price = self.data.get('gas_price')
        if listing and gas_price:
            res = self.vm.set_privileged(listing, gas_price)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_privileged(self, layout):
        layout.add_widget(Label('Get Privileged'), 0)
        layout.add_widget(Label(' '), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Call', self.get_privileged), 4)

    def get_privileged(self):
        res = self.vm.get_privileged()
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))
