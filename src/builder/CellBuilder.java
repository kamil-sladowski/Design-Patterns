package builder;


class CellBuilder extends AbstractCellBuilder{
    @Override
    public void createCellNucleus() {
        if(cell.getNucleus() == null)
            cell.setNucleus(new Nucleus());
    }

    @Override
    public void createCellMembrane() {
        cell.setMembrane(new Membrane());
    }

    @Override
    public void createNuclearMembrane() {
        cell.setNuclearMembrane(new NuclearMembrane());
    }

    @Override
    public void createCytoplasm() {
        cell.setCytoplasme(new Cytoplasme());
    }

    @Override
    public void createEndoplasmicReticulum() {
        cell.setEndoplasmicReticulum(new EndoplasmicReticulum());
    }

    @Override
    public void createRibosomes() {
        cell.setRibosome(new Ribosome());
    }

    @Override
    public void createMitochondria() {
        cell.setMitochonria(new Mitochonria());
    }

    @Override
    public void createVacuoles() {
        cell.setVocule(new Vocole());
    }

    public void createLysosomes(){
        cell.setLysosome(new Lysosome());
    }
}
