package builder;

abstract class AbstractCellBuilder{
    protected Cell cell;

    public void createNewCell(){
        cell = new Cell();
    }

    public abstract void createCellMembrane();
    public abstract void createCellNucleus();
    public abstract void createNuclearMembrane();
    public abstract void createCytoplasm();
    public abstract void createEndoplasmicReticulum();
    public abstract void createRibosomes();
    public abstract void createMitochondria();
    public abstract void createVacuoles();
    public abstract void createLysosomes();
}
