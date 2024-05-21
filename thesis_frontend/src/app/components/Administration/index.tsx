"use client"
import Image from 'next/image';
import Link from 'next/link';
import { ChevronRightIcon } from '@heroicons/react/24/outline';
import { Fade } from "react-awesome-reveal";


interface cardDataType {
    imgSrc: string;
    heading: string;
    subheading: string;
    // link: string;
    name:string;
}

const cardData: cardDataType[] = [
    {
        imgSrc: '/images/Features/directeur.jpg',
        heading: "Directeur",
        subheading: "Promeut l'excellence académique sur le plan national et international par des compétences administratives.",
        // link: 'Learn more',
        name:'Dr ADEGNI Mozart',

    },
    {
        imgSrc: '/images/Features/professeure.jpg',
        heading: "Professeure",
        subheading: "Enseigne des cours en utilisant des méthodes pédagogiques adaptées pour maximiser l'apprentissage des étudiants.",
        // link: 'Learn more',
        name:'Mme DAGAN Célia',

    },
    {
        imgSrc: '/images/Features/comptable.jpg',
        heading: "Comptable",
        subheading: "Assure la gestion efficace et la transparence financière de l'université grâce à des compétences techniques et analytiques.",
        // link: 'Learn more',
        name:'Mme VOSSA Anabelle',
    },
    {
        imgSrc: '/images/Features/directeuradjoint.jpg ',
        heading: "Directeur Adjoint",
        subheading: "Dans le soutien au directeur principal, il s'occupe de la gestion efficace des opérations de l'université sous son autorité.",
        // link: 'Learn more',
        name:'M SOGLO Baudouin',

    }

]

const Work = () => {
    return (


        <div>
            <div className='mx-auto max-w-7xl py-40 px-6' id="about-section" style={{marginTop:'-60px'}}>
                <div className='text-center mb-14' >
                    <Fade direction={'up'} delay={400} cascade damping={1e-1} triggerOnce={true}>
                        <h3 className='text-pink text-lg font-normal mb-3 ls-51 uppercase' >Administration</h3>
                    </Fade>
                    <Fade direction={'up'} delay={800} cascade damping={1e-1} triggerOnce={true}>
                        <p className='text-3xl lg:text-5xl font-semibold text-lightgrey'>Quelques membres de<br /> l´administration.</p>
                    </Fade>
                </div>


                <div className='grid sm:grid-cols-2 lg:grid-cols-4 gap-y-20 gap-x-5 mt-22'>
                    <Fade direction={'up'} delay={1000} cascade damping={1e-1} triggerOnce={true}>
                        {cardData.map((items, i) => (
                            <div className='card-b p-8 relative rounded-3xl' key={i}>
                                <div className='work-img-bg rounded-full flex justify-center'>
                                    <Image src={items.imgSrc} alt={items.imgSrc} width={300} height={300} />
                                </div>
                                <h3 className='text-2xl text-black font-semibold text-center mt-16'>{items.heading}</h3>
                                <p className='text-lg font-normal text-black text-center text-opacity-50 mt-2 '>{items.subheading}</p>
                                <div className='flex items-center justify-center'>
                                    <p className='text-center text-lg font-medium text-pink mt-2 hover-underline'>{items.name}</p>
                                </div> 
                            </div>
                        ))}
                    </Fade>
                </div>
            </div>
        </div>

    )
}

export default Work;
