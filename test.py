class MailBox:
    def collect_mail(self):
        print('Mail has been collected')

class SortingDepartment:
    def sort_mail(self):
        print('Mail is being sorted...')

class DeliveryTruck:
    def deliver_mail(self):
        print('Mail is being delivered')

class PostOfficeFacade:
    def __init__(self):
        self.mailbox = MailBox()
        self.sorting_department = SortingDepartment()
        self.delivery_truck = DeliveryTruck()

    def send_mail(self):
        print('Post Office is starting mail sending process')
        self.mailbox.collect_mail()
        self.sorting_department.sort_mail()
        self.delivery_truck.deliver_mail()
        print('Post Office has completed the mail sending process')

if __name__ == '__main__':
    post_office = PostOfficeFacade()
    post_office.send_mail()




"""
class House(PostOfficeFacade):
    def __init__(self, monkey_stuff, bam):
        super().__init__()
        self.monkey_stuff = monkey_stuff
        self.bam = bam
    
    def send_mail(self):
        print(self.bam, self.monkey_stuff)"""

"""    house = House('digger', 'bigger')
    house.send_mail()"""