from models.biodata_model import BioDataModel
from views.biodata_view import BioDataView


class BioDataController:
    def __init__(self, root):
        self.root = root
        self.model = BioDataModel()
        self.view = BioDataView(root)

    def run(self):
        biodata = self.model.get_biodata()
        self.view.show_card(biodata)
        self.root.mainloop()
