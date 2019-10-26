package builder;


import java.util.ArrayList;

class Cell{
    private CellWall cellWall = null;
    private Nucleus nucleus = null;

    private ArrayList<Chloroplasts> chloroplasts;
    private ArrayList<Lysosome> lysosome;
    private ArrayList<Membrane> membrane;
    private ArrayList<NuclearMembrane> nuclearMembrane;
    private ArrayList<Cytoplasme> cytoplasme;
    private ArrayList<EndoplasmicReticulum> endoplasmicReticulum;
    private ArrayList<Ribosome> ribosome;
    private ArrayList<Mitochonria> mitochonria;
    private ArrayList<Vocole> vocule;


    public Cell() {
        this.chloroplasts = new ArrayList<>();
        this.lysosome = new ArrayList<>();
        this.membrane = new ArrayList<>();
        this.nuclearMembrane = new ArrayList<>();
        this.cytoplasme = new ArrayList<>();
        this.endoplasmicReticulum = new ArrayList<>();
        this.ribosome = new ArrayList<>();
        this.mitochonria = new ArrayList<>();
        this.vocule = new ArrayList<>();
    }

    public void setCellWall(CellWall cellWall) {
        this.cellWall = cellWall;
    }

    public void setNucleus(Nucleus nucleus) {
        this.nucleus = nucleus;
    }

    public void setChloroplasts(Chloroplasts chloroplasts) {
        this.chloroplasts.add(chloroplasts);
    }

    public void setLysosome(Lysosome lysosome) {
        this.lysosome.add(lysosome);
    }

    public void setMembrane(Membrane membrane) {
        this.membrane.add(membrane);
    }

    public void setNuclearMembrane(NuclearMembrane nuclearMembrane) {
        this.nuclearMembrane.add(nuclearMembrane);
    }

    public void setCytoplasme(Cytoplasme cytoplasme) {
        this.cytoplasme.add(cytoplasme);
    }

    public void setEndoplasmicReticulum(EndoplasmicReticulum endoplasmicReticulum) {
        this.endoplasmicReticulum.add(endoplasmicReticulum);
    }

    public void setRibosome(Ribosome ribosome) {
        this.ribosome.add(ribosome);
    }

    public void setMitochonria(Mitochonria mitochonria) {
        this.mitochonria.add(mitochonria);
    }

    public void setVocule(Vocole vocule) {
        this.vocule.add(vocule);
    }

    public CellWall getCellWall() {
        return cellWall;
    }

    public Nucleus getNucleus() {
        return nucleus;
    }
}
